##################
Create Model Guide
##################

Veda Online provides a **Create Model** option that allows users to create a model directly from a GitHub repository. This can be done in two ways: clone a **public** repository by URL, or use a **GitHub Personal Access Token (PAT)** so Veda Online can list and clone repositories your account can access (including private repos).

Prerequisites
=============

* A `GitHub <https://github.com/>`_ account.
* For the **public repository** flow: the model must be in a **public** GitHub repository and you need its HTTPS URL.
* For the **PAT** flow: a PAT that can access the repositories you want to clone. For private repositories, the token typically needs the **repo** scope (or the fine-grained equivalent your organization requires). If the token cannot see a repo, it will not appear in the list after you save.

**Model visibility (Public / Private in Veda Online)**  
These options control **who can see the model inside Veda Online** (your workspace vs. shared more broadly), not whether the GitHub repository itself is public or private. Pick the option that matches how you want the model to appear to other Veda Online users.

Create Model from a Public Repository
======================================

Use this option when the model repository is publicly accessible on GitHub.

1. Log in to `Veda Online <https://vedaonline.cloud/Home.aspx>`_ and click **Create model**.
2. In the **Public GitHub repo** field, enter the repository **HTTPS** URL, for example: ``https://github.com/your-org/your-model-repo`` (use the browser address bar copy from the repo’s main page, or the **Code** button on GitHub).
3. Click **Get Branches**.
4. Select the branch you need from the branch dropdown.
5. Choose **privacy status** for the model in Veda Online (**Public** or **Private**—see above).
6. Click **Clone**.

After a successful clone, the new model should appear in your Veda Online workspace (for example in the model list or Navigator, depending on your layout) so you can open and work with it.

Create Model Using a GitHub Personal Access Token
===================================================

If you do not have a suitable token yet, create one first: `Create and store PAT <https://www.youtube.com/watch?v=28epMT27MJ4>`_. Ensure the token has permission to access the GitHub repositories that contain your Veda models.

1. Click **Create model**. For a video walkthrough, see `Create & model sync <https://www.youtube.com/watch?v=PtC7OWQaWY0>`_.
2. In the **Access your GitHub repositories** section, enter:

   - Your **GitHub username**
   - Your **GitHub Personal Access Token (PAT)**

3. Click **Save**.
4. After a successful save, the list of available model folders (repositories) loads in the **left-hand** panel.
5. In that list, select the **repository or folder** that contains your Veda model, then choose the **branch** you want (for example ``main`` or a release branch).
6. Choose **model visibility** (**Public** or **Private** in Veda Online—see above).
7. Click **Clone**.

After a successful clone, the model should appear in your Veda Online workspace so you can open it like any other model.

If something goes wrong
========================

* **Public URL path:** Confirm the URL is the HTTPS repo URL, the repository is **public**, and the branch exists on GitHub.
* **PAT path — empty or incomplete list:** Regenerate or adjust the token so it has the **scopes** required for your repos; confirm the **username** matches the account that owns the token.
* **PAT path — organization repos missing:** Your org may restrict third-party access; approve Veda Online / the token in GitHub **organization** settings if prompted.
* **Wrong or outdated branch:** Use **Get Branches** (public flow) or re-select the branch after the list refreshes (PAT flow).
