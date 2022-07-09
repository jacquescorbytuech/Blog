const htmlmin = require('html-minifier')

const now = String(Date.now())

const pluginRss = require("@11ty/eleventy-plugin-rss");
const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

module.exports = function (eleventyConfig) {
  eleventyConfig.addWatchTarget('./styles/tailwind.config.js')
  eleventyConfig.addWatchTarget('./styles/tailwind.css')
  eleventyConfig.addPlugin(pluginRss);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  eleventyConfig.addShortcode('version', function () {
    return now
  })

  eleventyConfig.addCollection("test", function (collectionApi) {
    return collectionApi.getFilteredByGlob("_posts/writing/*.md");
  });

  eleventyConfig.addCollection("reading", function (collectionApi) {
    return collectionApi.getFilteredByGlob("_posts/reading/*.md");
  });
  
  eleventyConfig.addCollection("links", function (collectionApi) {
    return collectionApi.getFilteredByGlob("_posts/links/*.md");
  });

  eleventyConfig.addTransform('htmlmin', function (content, outputPath) {
    if (
      process.env.ELEVENTY_PRODUCTION &&
      outputPath &&
      outputPath.endsWith('.html')
    ) {
      let minified = htmlmin.minify(content, {
        useShortDoctype: true,
        removeComments: true,
        collapseWhitespace: true,
      })
      return minified
    }

    return content
  })

}