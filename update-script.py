#!/usr/bin/env python3
import os
import sys
import yaml
import datetime
import subprocess
from pathlib import Path
from collections import defaultdict

# Assuming script is run from repo root
REPO_PATH = Path(".")
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

def load_yaml_file(file_path):
    """Load a YAML file and return its contents."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml_file(file_path, data):
    """Save data to a YAML file."""
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def find_topic_in_modules(topic_id):
    """Find which module file contains the specified topic ID."""
    master_plan = load_yaml_file(REPO_PATH / "master_plan.yaml")
    
    # Check all module files
    for module in master_plan.get("modules", []):
        module_file = REPO_PATH / module["file"]
        if module_file.exists():
            module_data = load_yaml_file(module_file)
            
            # Search for the topic or subtopic in this module
            for topic in module_data.get("topics", []):
                if topic["id"] == topic_id:
                    return module["file"], module_data, topic, None, master_plan
                
                # Check subtopics
                for subtopic in topic.get("subtopics", []):
                    if subtopic["id"] == topic_id:
                        return module["file"], module_data, topic, subtopic, master_plan
    
    return None, None, None, None, None

def update_module_status(module_name, master_plan, status="active"):
    """Update a module's status in the master plan and update active_modules list."""
    updated = False
    for module in master_plan.get("modules", []):
        if module["name"] == module_name:
            if module["status"] != status:
                module["status"] = status
                updated = True
                
                # Update the active_modules list in metadata
                if status == "active":
                    active_modules = master_plan.get("metadata", {}).get("active_modules", [])
                    if module["name"] not in active_modules:
                        active_modules.append(module["name"])
                        master_plan["metadata"]["active_modules"] = active_modules
                
                print(f"Updated module {module_name} status to {status}")
    return updated

def update_session_count(master_plan):
    """Increment the sessions_completed count in metadata."""
    metadata = master_plan.get("metadata", {})
    sessions = metadata.get("sessions_completed", 0)
    metadata["sessions_completed"] = sessions + 1
    metadata["last_updated"] = TODAY
    return True

def parse_command(command_str):
    """Parse the entire command string into multiple update operations."""
    if "COMMIT" in command_str:
        updates_part, commit_part = command_str.split("COMMIT", 1)
        commit_message = commit_part.strip()
    else:
        updates_part = command_str
        commit_message = f"Update learning progress - {TODAY}"
    
    parts = updates_part.split("UPDATE")
    
    # Filter out empty parts and parse each UPDATE command
    updates = []
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        topic_id = None
        topic_updates = {}
        
        for item in part.split():
            if '=' not in item:
                continue
                
            key, value = item.split('=', 1)
            
            if key == "topic":
                topic_id = value
            elif key == "mastery":
                topic_updates[key] = int(value)
            elif key == "date":
                date_value = value
                topic_updates["last_practiced"] = date_value
                # For attempts, we'll add to the list rather than replace
                topic_updates["attempts"] = date_value
            else:
                topic_updates[key] = value
        
        if topic_id and topic_updates:
            updates.append((topic_id, topic_updates))
    
    return updates, commit_message

def process_updates(updates):
    """Process all updates, grouping them by module file."""
    # Track changes to files and master plan
    updated_files = set()
    master_plan = None
    session_increment_needed = False
    
    for topic_id, topic_updates in updates:
        module_file, module_data, topic, subtopic, master_plan = find_topic_in_modules(topic_id)
        
        if not module_file:
            print(f"Error: Topic {topic_id} not found in any module.")
            continue
        
        # Determine if we're updating a topic or subtopic
        target = subtopic if subtopic else topic
        
        # Check if this is a status change that affects module activation
        if "status" in topic_updates and not subtopic:
            # If a top-level topic is being covered for the first time
            if target["status"] == "uncovered" and topic_updates["status"] in ["in-progress", "covered"]:
                # Find the module in master_plan that contains this file
                for module in master_plan.get("modules", []):
                    if module["file"] == module_file:
                        update_module_status(module["name"], master_plan)
                        break
            
            # A status change indicates a session was completed
            session_increment_needed = True
        
        # Apply updates
        for key, value in topic_updates.items():
            if key == "attempts":
                if "attempts" not in target or not target["attempts"]:
                    target["attempts"] = []
                target["attempts"].append(value)
            else:
                target[key] = value
        
        # Save the updated file
        save_yaml_file(REPO_PATH / module_file, module_data)
        updated_files.add(module_file)
        print(f"Updated {topic_id} in {module_file}")
    
    # Update session count and master plan if needed
    if master_plan:
        if session_increment_needed:
            update_session_count(master_plan)
        save_yaml_file(REPO_PATH / "master_plan.yaml", master_plan)
        updated_files.add("master_plan.yaml")
    
    return len(updated_files) > 0

def git_commit_and_push(commit_message):
    """Commit all changes and push to GitHub."""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Successfully committed and pushed changes: {commit_message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_learning.py \"UPDATE topic=ID status=X mastery=Y date=Z [UPDATE ...] COMMIT message\"")
        return
    
    command = sys.argv[1]
    updates, commit_message = parse_command(command)
    
    if not updates:
        print("No valid update commands found")
        return
    
    # Apply all updates
    if process_updates(updates):
        git_commit_and_push(commit_message)
    else:
        print("No updates were applied")

if __name__ == "__main__":
    main()
