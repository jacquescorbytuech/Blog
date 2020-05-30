# Static Site

[![Netlify Status](https://api.netlify.com/api/v1/badges/3ab84d8a-8d7c-43c7-98ef-a66ae301ce0d/deploy-status)](https://app.netlify.com/sites/relaxed-albattani-580cf2/deploys)

A simple personal website and blog built using the Pelican static site generator.

## Deployment

Run the following commands to generate the site:

### Dev deployment

Used to generate local test versions of the site during development.

    pelican content

### Final deployment

Used to generate the final version of the site, ready to publish to a hosting service.

    pelican content -s publishconf.py




    venv/Scripts/activate
    cd site  