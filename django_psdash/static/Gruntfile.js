var path = require('path'),
    ext = function (file) {
      return path.extname(file).slice(1);
    };

module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      build: {
        src: 'src/js/main.js',
        dest: 'psdash/js/main.min.js'
      }
    },
    cssmin: {
      minify: {
        expand: true,
        cwd: 'src/css/',
        src: ['*.css'],
        dest: 'psdash/css/',
        ext: '.min.css'
      }
    },
    bower: {
      build: {
        dest: 'psdash/vendor/',
        js_dest: 'psdash/vendor/js',
        css_dest: 'psdash/vendor/css',
        options: {
          packageSpecific: {
            bootstrap: {
              dest: 'psdash/vendor/fonts'
            }
          }
        }
      }
    },
    injector: {
      options: {
        addRootSlash: false,
        transform: function (filepath) {
          var e = ext(filepath);
          if (e === 'css') {
            return '<link rel="stylesheet" href="{% static "' + filepath + '" %}">';
          } else if (e === 'js') {
            return '<script src="{% static "' + filepath + '" %}"></script>';
          }
          return '';
        }
      },
      local_dependencies: {
        files: {
          '../templates/psdash/index.html': ['psdash/**/*.js',
                                             'psdash/**/*.css']
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-bower');
  grunt.loadNpmTasks('grunt-asset-injector');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('default', ['uglify', 'cssmin', 'bower', 'injector']);
};
