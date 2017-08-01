const path = require('path');
const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const autoprefixer = require('autoprefixer');

module.exports = {
    // Entry point of our app where we import diff styles
    entry: {
        'app': './index.js'
    },
    // Where it will put them in our project
    output: {
        path: path.resolve( __dirname, '../static' ),
        filename: '[name].js',
    },
    // understand js path
    resolve: {
        extensions: ['.js']
    },
    // add modules
    module: {
        rules: [
            {
                test: /\.(sass|scss)$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        {
                            loader: 'css-loader'
                        },
                        {
                            loader: 'postcss-loader',
                            options: {
                                plugins: () => [autoprefixer]
                            }
                        },
                        {
                            loader: 'sass-loader'
                        },
                    ]
                })
            },

            {
                test: /\.(css)$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        {
                            loader: 'css-loader'
                        },
                        {
                            loader: 'postcss-loader',
                            options: {
                                plugins: () => [autoprefixer]
                            }
                        },
                    ]
                })
            },
            /**
             *  File loader for supporting images, for example, in CSS files.
             */
            {
                test: /\.(jpg|png|gif|ttf|eot)$/,
                use: 'file-loader'
            },
            {
                test: /\.(woff|ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: "file-loader"
            },
        ]
    },

    plugins: [
        new ExtractTextPlugin('style.css'),
        new CopyWebpackPlugin([
            {
                'from': path.resolve( __dirname, 'js/owl.carousel.min.js'),
                'to': path.resolve( __dirname, '../static' ),
                'force': true
            },
            {
                'from': path.resolve( __dirname, 'styles'),
                'to': path.resolve( __dirname, '../static' ),
                'force': true
            },
            {
                'from': path.resolve( __dirname, 'img'),
                'to': path.resolve( __dirname, '../static' ),
                'force': true
            }
        ])
    ]
};
