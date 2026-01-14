# Debugging Self-Healing CI

## Steps to Debug:

### 1. Check if API Keys are Set
Go to: https://github.com/nandanadileep/test/settings/secrets/actions

You should see:
- ✅ GEMINI_API_KEY
- ✅ GROQ_API_KEY

If missing, add them:
1. Click "New repository secret"
2. Add GEMINI_API_KEY with your Gemini API key
3. Add GROQ_API_KEY with your Groq API key

### 2. Check Recent Workflow Runs
Go to: https://github.com/nandanadileep/test/actions

Look for failed runs and click on them to see:
- Did "Run test suite" fail? (expected)
- Did "Run self-healing agent" step exist and run?
- Did it show any errors about missing API keys?
- Did "Push auto-fix commit" succeed?

### 3. Check Agent Logs
In the workflow run details, expand:
- "Run self-healing agent" step
- Look for errors like:
  - `KeyError: 'GEMINI_API_KEY'`
  - `KeyError: 'GROQ_API_KEY'`
  - Agent execution errors

### 4. Common Issues:

**Issue**: Workflow shows green checkmark even though tests fail
- **Cause**: The workflow has `continue-on-error: true` on test step
- **Expected**: Should run auto-fix, then verify

**Issue**: Auto-fix step doesn't appear
- **Cause**: Commit message contains `[ci-auto-fix]`
- **Solution**: Make a new commit without that string

**Issue**: Agent doesn't push fixes
- **Cause**: Agent failed to create fix or API keys missing
- **Check**: Agent logs in workflow run

## What Should Happen:

1. ✅ Tests run and fail
2. 🤖 Agent analyzes build.log
3. 🔧 Agent modifies code to fix tests
4. 💾 Agent commits with `[ci-auto-fix]` message
5. 📤 Agent pushes commit
6. ✅ Workflow runs tests again to verify
7. ✅ Second run skips agent (due to `[ci-auto-fix]` in message)
