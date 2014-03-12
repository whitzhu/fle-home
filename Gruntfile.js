module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'), //To read the values of the package.json file
    less: {
      compile: {
        options: {
          paths:["./fle_site/static/less"], //Directory to check for @imports
          yuicompress: true,
          strictImports: true //Force evaluation of imports.
        },
        files: {
          // target.css file: source.less file
          "fle_site/static/css/styles.css": "fle_site/static/less/styles.less"
        }
      }
    }
  });
 
  grunt.loadNpmTasks('grunt-contrib-less');
 
  grunt.registerTask('default', ['less']);
};