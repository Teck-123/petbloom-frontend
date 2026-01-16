# Tasks for Person 1 - Easy Work

## Your Job: Add comments to components

### Step 1: Setup (Copy-paste these commands)
```bash
git checkout dev
git pull origin dev
git checkout -b feature/person1-comments
```

### Step 2: Do These Simple Tasks (Each is 1 commit)

#### Task A: Add comment to Header.jsx
Open `src/components/Header.jsx`
Add this comment at the top (line 1):
```javascript
// Header component - Main navigation bar with user menu
```
Then run:
```bash
git add src/components/Header.jsx
git commit -m "Add documentation comment to Header component"
```

#### Task B: Add comment to Footer.jsx
Open `src/components/Footer.jsx`
Add this comment at the top (line 1):
```javascript
// Footer component - Site footer with links and contact info
```
Then run:
```bash
git add src/components/Footer.jsx
git commit -m "Add documentation comment to Footer component"
```

#### Task C: Add comment to ProtectedRoute.jsx
Open `src/components/ProtectedRoute.jsx`
Add this comment at the top (line 1):
```javascript
// ProtectedRoute component - Guards routes requiring authentication
```
Then run:
```bash
git add src/components/ProtectedRoute.jsx
git commit -m "Add documentation comment to ProtectedRoute component"
```

### Step 3: Push to GitHub
```bash
git push origin feature/person1-comments
```

### Step 4: Create Pull Request
1. Go to GitHub repository
2. Click "Compare & pull request"
3. Make sure base is `dev`
4. Click "Create Pull Request"

✅ DONE! You now have 3 commits showing your work!
