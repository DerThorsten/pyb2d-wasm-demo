const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const webpack = require('webpack');
const MonacoWebpackPlugin = require('monaco-editor-webpack-plugin');

const path = require('path');

module.exports = {
	module: {
		rules: [
      {
  			test: /\.css$/,
  			use: [
  				'style-loader',
  				'css-loader'
  			]
  		},
      {
        test: /\.ttf$/,
        use: ['file-loader']
      },
      // bootstrap stuff
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: () => [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      }
    ]
	},
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
			patterns: [{
				from: 'src/pyjs_runtime_browser.wasm',
				to: '.'
			}, {
				from: 'src/*.data',
				to: "[name][ext]",
			}, ]
		},
    new MonacoWebpackPlugin({
      languages: ['typescript', 'javascript', 'css', 'json','python']
    })
    )
	],
	mode: 'development',
	target: 'web',
	output: {
		clean: true,
    path: path.resolve(__dirname, 'dist'),
    filename: 'app.js'
	},
	devServer: {
		static: './dist',
		open: true
	}
};