const path = require('path');
function resolve (dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  lintOnSave: true,
  chainWebpack: (config)=>{
    config.resolve.alias
        .set('@$', resolve('src'))
        .set('assets',resolve('src/assets'))
        .set('components',resolve('src/components'))
        .set('layout',resolve('src/layout'))
        .set('base',resolve('src/base'))
        .set('static',resolve('src/static'))
        .set('views',resolve('src/views'))
        .set('network',resolve('src/network'))
  }
}


// module.exports = {
//   configureWebpack: {
//     resolve: {
//       extensions: [],
//       alias: {
//         // '@' 默认为'src',
//         'assets': '@/assets',
//         // 'common': '@/common',
//         'components': '@/components',
//         // 'network': '@/network',
//         'views': '@/views'
//       }
//     }
//   }
// }