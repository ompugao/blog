# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Hugo-based personal blog using the Ezhil theme. The site is configured for Japanese content (`ja-JP`).

## Development Commands

### Building and Serving
```bash
# Serve the site locally with live reload
mise x hugo -- hugo server

# Serve with drafts included
mise x hugo -- hugo server -D

# Build the site for production
mise x hugo -- hugo

# Build with minification
mise x hugo -- hugo --minify
```

### Content Management
```bash
# Create a new post
mise x hugo -- hugo new posts/post-title.md

# Create a new page
mise x hugo -- hugo new page-name.md
```

## Site Structure

- `hugo.toml` - Main configuration file with site settings, theme configuration, and menu structure
- `content/` - Markdown content files (currently empty, all content creation needed)
- `static/` - Static assets (CSS, JS, images) that are copied directly to output
- `layouts/` - Custom layout overrides (if needed)
- `themes/ezhil/` - The Ezhil theme submodule/directory
- `public/` - Generated site output (git ignored, created by Hugo build)

## Theme Configuration

The site uses the Ezhil theme with these key customizations in `hugo.toml`:
- Japanese language (`ja-JP`)
- Pagination set to 10 posts
- Summary length of 20 characters
- Custom CSS/JS support configured
- Social media links for GitHub and Twitter
- Main navigation menu with Home, All posts, About, and Tags

## Content Types

- **Posts**: Place in `content/posts/` directory, included in recent posts
- **Pages**: Use `type: "page"` in frontmatter, excluded from recent posts
- **About**: Configure in `content/about.md` as a page type

## Deployment

The site is configured for deployment to `https://blog.ompugao.com/`. The `public/` directory contains the built site ready for deployment to any static hosting service.

## Development Notes

- No package.json present - this is a pure Hugo site
- Theme is included as a directory (not a git submodule)
- Custom CSS and dark CSS files are referenced but need to be created in `static/css/`
- Custom JS files are referenced but need to be created in `static/js/`
