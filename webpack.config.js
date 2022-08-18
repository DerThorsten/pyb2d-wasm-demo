const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const webpack = require('webpack');

const path = require('path');

module.exports = {
  plugins: [
    new webpack.ProvidePlugin({
           $: "jquery",
           jQuery: "jquery"
    }),
    new HtmlWebpackPlugin({
      hash: true,
      title: 'Webpack Example App',
      header: 'Webpack Example Title',
      metaDesc: 'Webpack Example Description',
      template: './src/index.html',
      filename: 'index.html',
      inject: 'body'
    }),
    new CopyPlugin({
      patterns: [
        {
          from: 'src/pyjs_runtime_browser.wasm',
          to: '.'
        },
        {
          from: 'src/*.data',
          to: "[name][ext]",
        },
      ]
    })
  ],
  mode: 'development',
  watch: true, // Enable watch mode
  target: 'web',
  output: {
    clean: true
  },
  devServer: {
    static: './dist',
    open: true
  }
};