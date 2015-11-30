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
    },
    'safesync_url': ''
  }
]
