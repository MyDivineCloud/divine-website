# Divine Website

A tiny, deliberately insecure repository for testing static analysis and repository-configuration checks.

## Safety

The code under `examples/` is a set of test fixtures, not a website or service. It is intentionally unsafe, has no network listener or deployment setup, and must not be copied into production or exposed to untrusted input.

## Included test cases

- SQL query built with string interpolation
- Unescaped HTML output
- Shell command built from input and run with a shell
- Weak MD5 hashing

## Intentional repository gaps

This repository has no CI workflow, dependency-update configuration, security policy, or code-ownership rules. These omissions are intentional so repository scanners can report them.
