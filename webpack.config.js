const path = require('path');
const webpack = require("webpack");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require("webpack-bundle-tracker");


module.exports = {
  entry: {
    main: './src/static/js/index.js',
    sshock_dashboard: './src/static/pages/sshock/dashboard/index.js',
    account_publickey: './src/static/pages/account/sshpublickey/index.js',
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
