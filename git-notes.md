 `git fetch`

- **Description**: Downloads updates from the remote repository (e.g., commits, branches, tags) but **does not affect your local branch**.
- **Usage**:  
  ```bash
  git fetch origin
  ```

- **When to Use**: Use when you want to inspect changes from the remote repository without merging them into your local branch.

`git pull`

- **Description**: Equivalent to **git fetch** followed by **git merge**. Downloads updates and immediately merges them into your current branch..
- **Usage**:  
  ```bash
  git pull origin main
  ## or master
  ```

- **When to Use**: Use when you are ready to automatically fetch and merge remote changes into your local branch in one step.