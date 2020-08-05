# moveDetector

- the main file is Main.py
- it runs 2 Processes:  
    - Diff process
    - Display process
- Main:
  - sends frames from the video capture to the Diff process, and
  - sends frames to the Display Process

- Diff Process:
  - detects motion in the frames by analyzing diffs
  - sends the marked motion to the Display Process
 
- Display Process
  - merges rgb and marked motions (gray) and displays the merged images
  
  
  
