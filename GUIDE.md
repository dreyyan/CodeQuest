# SETUP/SUBMISSION GUIDE
## SETUP
1. Clone the repository:
``` bash
git clone https://github.com/dreyyan/https://github.com/dreyyan/CodeQuest
```

2. Navigate to `/{YourProgrammingLanguage}/{CurrentLevel}`:
``` bash
cd Python/level_1
```

3. Remove the other Programming Language folder:
- If JavaScript, remove `/Python`
- If Python, remove `/JavaScript`

``` bash
git rm -r Python
```

## SUBMISSION
1. Create a new branch (your own code version):
``` bash
git checkout -b submission-name
```

2. Add your changes:
``` bash
git add .
```

3. Commit (ready for submission) your changes:
``` bash
git commit -m "Added submission for your-name"
```

4. Push (save your changes) the branch to the repository:
``` bash
git push origin submission-name
```