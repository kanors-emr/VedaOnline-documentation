---
description: User Profile in Veda Online — save GitHub credentials for Pull, Push, and Excel Viewer save.
---

# User Profile

Open **User Profile** from the user menu (top right) while you are signed in.

## GitHub credentials

Veda Online uses a GitHub **token** (Personal Access Token) like a password, so it can Pull private repositories, Push Excel files, and **Save** in Excel Viewer.

How to create a token: [Create and store PAT](https://www.youtube.com/watch?v=28epMT27MJ4) (also covered in the [Create Model Guide](Create-Model-Guide.md)).

1. Open User Profile.
2. Under **GitHub Credentials**, enter your GitHub username and token.
3. Click **Save**.

To replace a token, save the new values. To remove a saved token, click **Remove**.

- **Push** needs a token that can update that repository. If the token is missing or cannot update the repo, Push shows an error and does not open the file list.
- **Pull** and **Start from Scratch** need a token for **private** repositories. Public repositories do not.
- **Excel Viewer**: you can open a file without a token. Save needs a saved token, and GitHub must not have newer files than this model folder. See [Excel Viewer](model_workspace/Navigator.md#excel-viewer).

!!! note

    Other User Profile options will be documented here later.
