solutions = [
  {
    'name': 'src',
    'url': 'https://chromium.googlesource.com/chromium/src.git',
    'deps_file': '.DEPS.git',
    'managed': False,
    'custom_deps': {
      'src/third_party/adobe/flash/binaries/ppapi/linux': None,
      'src/third_party/adobe/flash/binaries/ppapi/linux_x64': None,
      'src/third_party/adobe/flash/symbols/ppapi/linux': None,
      'src/third_party/adobe/flash/symbols/ppapi/linux_x64': None,
      'src/third_party/WebKit': None,
    },
    'safesync_url': ''
  },
  {
    'name': 'src-internal',
    'url': 'https://chrome-internal.googlesource.com/chrome/src-internal.git',
    'deps_file': '.DEPS.git',
    'custom_deps': {
      'src/data/esctf': None,
      'src/data/memory_test': None,
      'src/data/mozilla_js_tests': None,
      'src/data/page_cycler': None,
      'src/data/tab_switching': None,
      'src/data/saved_caches': None,
      'src/data/selenium_core': None,
      'src/tools/grit/grit/test/data': None,
      'src/tools/perf/data': None,
      'src/gpu/gles2_conform_test': None,
      'src/third_party/gles2_conform': None
    }
  }
]
