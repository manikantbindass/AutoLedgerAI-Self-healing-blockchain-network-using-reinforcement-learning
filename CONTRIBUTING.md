# Contributing to AutoLedgerAI

Thank you for your interest in contributing to **AutoLedgerAI** – Self-Healing Blockchain Network with Reinforcement Learning! 🎉

We welcome contributions from developers, researchers, and blockchain enthusiasts. This guide will help you get started.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Issue Reporting](#issue-reporting)
- [Community](#community)

---

## 📜 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and constructive in all interactions.

**Key Principles:**
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Assume good intentions
- Focus on what's best for the community
- Show empathy towards other community members

---

## 🤝 How Can I Contribute?

There are many ways to contribute to AutoLedgerAI:

### 1. 🐛 Report Bugs
Found a bug? Please [open an issue](https://github.com/manikantbindass/AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning/issues/new) with:
- Clear description of the bug
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots or logs (if applicable)

### 2. 💡 Suggest Enhancements
Have an idea for a new feature? Open an issue with the `enhancement` label and describe:
- The problem your feature solves
- Proposed solution
- Alternative solutions considered
- Why this would benefit the project

### 3. 📝 Improve Documentation
Documentation is critical! You can help by:
- Fixing typos or unclear explanations
- Adding examples and tutorials
- Improving API documentation
- Translating docs to other languages

### 4. 🔧 Submit Code Changes
Ready to code? Great! See the [Development Workflow](#development-workflow) section below.

### 5. 🧪 Write Tests
Help us improve test coverage by:
- Adding unit tests for existing code
- Writing integration tests
- Creating test scenarios for edge cases

### 6. 🎨 Design Improvements
Contribute to the frontend dashboard:
- UI/UX improvements
- New visualizations
- Accessibility enhancements

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

```bash
# Required
Python 3.9+
Node.js 16+
Docker & Docker Compose
Git

# Optional (for local development)
MongoDB
Kafka
Redis
```

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:

```bash
git clone https://github.com/YOUR_USERNAME/AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning.git
cd AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning
```

3. **Add upstream remote**:

```bash
git remote add upstream https://github.com/manikantbindass/AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning.git
```

### Install Dependencies

```bash
# Backend dependencies
cd backend
pip install -r requirements.txt

# RL Agent dependencies
cd ../rl-agent
pip install -r requirements.txt

# Frontend dependencies
cd ../frontend/dashboard
npm install

# Return to root
cd ../..
```

### Setup Environment

```bash
# Copy environment template
cp configs/env.example .env

# Edit .env with your local configuration
nano .env
```

### Run Locally

```bash
# Option 1: Docker Compose (recommended)
docker-compose up --build

# Option 2: Manual setup
# Terminal 1 - Backend
cd backend && python main.py

# Terminal 2 - RL Agent
cd rl-agent && python training/train_dqn.py

# Terminal 3 - Frontend
cd frontend/dashboard && npm start
```

---

## 🔄 Development Workflow

### 1. Create a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

**Branch Naming Convention:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `test/` - Test additions/changes
- `refactor/` - Code refactoring
- `chore/` - Maintenance tasks

### 2. Make Your Changes

- Write clean, readable code
- Follow the [Coding Standards](#coding-standards)
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run unit tests
pytest tests/

# Run integration tests
pytest tests/integration/

# Run linting
flake8 .
black --check .

# Run type checking
mypy .
```

### 4. Commit Your Changes

Follow the [Commit Message Guidelines](#commit-message-guidelines):

```bash
git add .
git commit -m "feat: add trust score visualization to dashboard"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] Code follows project coding standards
- [ ] All tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated documentation
- [ ] Commit messages follow guidelines
- [ ] No merge conflicts with `main` branch

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issue
Fixes #(issue number)

## How Has This Been Tested?
Describe the tests you ran to verify your changes.

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] My code follows the project style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
```

### Review Process

1. A maintainer will review your PR within 48 hours
2. Address any requested changes
3. Once approved, a maintainer will merge your PR
4. Your contribution will be included in the next release!

---

## 💻 Coding Standards

### Python Code

- **Style**: Follow [PEP 8](https://pep8.org/)
- **Formatter**: Use `black` with default settings
- **Linter**: Use `flake8`
- **Type Hints**: Use type hints for function signatures
- **Docstrings**: Use Google-style docstrings

**Example:**

```python
def calculate_trust_score(
    node_id: str,
    metrics: Dict[str, float],
    history: List[float]
) -> float:
    """
    Calculate dynamic trust score for a node.
    
    Args:
        node_id: Unique identifier for the node
        metrics: Current performance metrics
        history: Historical trust scores
        
    Returns:
        Computed trust score between 0.0 and 1.0
        
    Raises:
        ValueError: If metrics are invalid
    """
    # Implementation
    pass
```

### JavaScript/React Code

- **Style**: Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- **Formatter**: Use `prettier`
- **Linter**: Use `eslint`
- **Components**: Use functional components with hooks
- **Naming**: PascalCase for components, camelCase for functions

**Example:**

```javascript
/**
 * Trust Score Visualization Component
 * @param {Object} props - Component props
 * @param {Array} props.nodes - Array of node objects
 * @param {Function} props.onNodeClick - Callback when node is clicked
 */
const TrustScoreChart = ({ nodes, onNodeClick }) => {
  // Implementation
};
```

### General Guidelines

- Keep functions small and focused (< 50 lines)
- Use meaningful variable and function names
- Avoid deep nesting (max 3 levels)
- Write self-documenting code
- Add comments for complex logic
- Remove commented-out code before committing
- No hardcoded credentials or secrets

---

## 🧪 Testing Guidelines

### Test Structure

```
tests/
├── unit/           # Unit tests for individual functions
├── integration/    # Integration tests for modules
├── e2e/           # End-to-end tests
└── fixtures/      # Test data and mocks
```

### Writing Tests

```python
import pytest
from blockchain.core.block import Block

class TestBlock:
    """Test suite for Block class"""
    
    def test_block_creation(self):
        """Test that a block can be created successfully"""
        block = Block(
            index=1,
            timestamp=1234567890,
            transactions=[],
            previous_hash="0" * 64
        )
        assert block.index == 1
        assert len(block.hash) == 64
    
    def test_block_mining(self):
        """Test proof of work mining"""
        block = Block(1, 1234567890, [], "0" * 64)
        block.mine_block(difficulty=2)
        assert block.hash.startswith("00")
```

### Test Coverage

- Aim for **80%+ code coverage**
- All new features must include tests
- Critical paths require 100% coverage

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_block.py

# Run with coverage report
pytest --cov=. --cov-report=html

# Run only failed tests
pytest --lf
```

---

## 📝 Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

### Examples

```bash
# Feature
feat(rl-agent): add PPO algorithm for consensus optimization

# Bug fix
fix(blockchain): resolve hash collision in block validation

# Documentation
docs(readme): update installation instructions for Windows

# Breaking change
feat(api)!: change trust score endpoint to return detailed metrics

BREAKING CHANGE: trust score endpoint now returns object instead of number
```

### Rules

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor" not "moves cursor")
- First line should be ≤ 72 characters
- Reference issues and PRs in the footer
- Explain **what** and **why**, not **how**

---

## 🐛 Issue Reporting

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.9.7]
- Docker Version: [e.g., 20.10.8]

**Additional context**
Any other relevant information.
```

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions you thought about.

**Additional context**
Any other relevant information.
```

---

## 🌍 Community

### Get Help

- **GitHub Discussions**: Ask questions and share ideas
- **Discord**: Join our [Discord server](#) (coming soon)
- **Stack Overflow**: Tag questions with `autoledgerai`

### Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for a list of amazing contributors!

### License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

## 🎯 Areas Looking for Contributions

We especially welcome contributions in these areas:

- [ ] **Multi-chain support** - Extend to support multiple blockchain networks
- [ ] **Federated RL** - Implement multi-agent reinforcement learning
- [ ] **Advanced anomaly detection** - Improve detection algorithms
- [ ] **Performance optimization** - Speed up consensus and validation
- [ ] **Security auditing** - Help identify and fix vulnerabilities
- [ ] **Mobile dashboard** - Create mobile-responsive UI
- [ ] **Documentation translations** - Translate docs to other languages
- [ ] **Tutorials and examples** - Create learning resources

---

## 🙏 Thank You!

Your contributions make AutoLedgerAI better for everyone. We appreciate your time and effort!

**Questions?** Reach out to the maintainers:
- **Manikant Kumar** - [@manikantbindass](https://github.com/manikantbindass)
- Email: [manikantbindass@gmail.com](mailto:manikantbindass@gmail.com)

---

**Happy Contributing! 🚀**
