const path = require('path');
const webpack = require("webpack");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require("webpack-bundle-tracker");


module.exports = {
  entry: {
    main: './src/static/js/index.js',
    account_dashboard: './src/static/pages/account/dashboard/index.js',
    account_publickey: './src/static/pages/account/publickey/index.js',
    userarea_device_list: './src/static/pages/userarea/device/list.js',
    userarea_device_create: './src/static/pages/userarea/device/create.js',
    userarea_device_delete: './src/static/pages/userarea/device/delete.js',
    userarea_keygroup_list: './src/static/pages/userarea/keygroup/list.js',
    userarea_keygroup_create: './src/static/pages/userarea/keygroup/create.js',
    userarea_keygroup_delete: './src/static/pages/userarea/keygroup/delete.js',
    userarea_keygroup_edit: './src/static/pages/userarea/keygroup/edit.js',
    userarea_publickey_list: './src/static/pages/userarea/publickey/list.js',
    userarea_publickey_delete: './src/static/pages/userarea/publickey/delete.js',
    userarea_publickey_update: './src/static/pages/userarea/publickey/update.js',
    userarea_publickey_create: './src/static/pages/userarea/publickey/create.js',
    adminarea_appintegration_list: './src/static/pages/adminarea/appintegration/list.js',
    adminarea_appintegration_create: './src/static/pages/adminarea/appintegration/create.js',
    adminarea_appintegration_delete: './src/static/pages/adminarea/appintegration/delete.js',
    adminarea_appintegration_detail: './src/static/pages/adminarea/appintegration/detail.js',
    superarea_host_list: './src/static/pages/superarea/host/list.js',
    superarea_host_create: './src/static/pages/superarea/host/create.js',
    superarea_host_delete: './src/static/pages/superarea/host/delete.js',
    superarea_hostgroup_list: './src/static/pages/superarea/hostgroup/list.js',
    superarea_hostgroup_create: './src/static/pages/superarea/hostgroup/create.js',
    superarea_hostgroup_delete: './src/static/pages/superarea/hostgroup/delete.js',
    superarea_publishgroup_create: './src/static/pages/superarea/publishgroup/create.js',
    superarea_publishgroup_delete: './src/static/pages/superarea/publishgroup/delete.js',
    superarea_publishgroup_list: './src/static/pages/superarea/publishgroup/list.js',
    superarea_publishgroup_detail: './src/static/pages/superarea/publishgroup/detail.js',

  },
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: '[name].js'
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
      //chunkFilename: devMode ? '[id].css' : '[id].[hash].css',
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
    }),
    new BundleTracker({filename: "./webpack-bundle.json"})
  ],
  module: {
    rules: [
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              hmr: process.env.NODE_ENV === 'development',
            },
          },
          'css-loader',
          //'postcss-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.svg$/,
        loader: 'svg-inline-loader'
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/'
            }
          }
        ]
      },
      {
          test: /\.(png|jpe?g|gif)$/i,
          use: [
              {
                  loader: 'file-loader',
              },
          ],
      },

    ]
  }
};
