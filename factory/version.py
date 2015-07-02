"""Version Module

So we only have to maintain version information in one place!
"""

version_info = (0, 0, 1)  # (major, minor, patch, dev?)
version = (
    ".".join(map(str, version_info))
    if version_info[-1] != "dev"
    else "dev"
)
