solutions = [
  {
    'name': 'src',
    'url': 'https://chromium.googlesource.com/chromium/src.git',
    'deps_file': '.DEPS.git',
    'managed': False,
    'custom_deps': {
      'src/third_party/WebKit': None,
    },
    'safesync_url': ''
  }]