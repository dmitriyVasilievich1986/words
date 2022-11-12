const webpack = require("webpack");

module.exports = (env, argv) => {
  return {
    entry: "./src/index.js",
    output: {
      filename: "main.js",
    },
    devtool: argv.mode === "development" ? "source-map" : "eval",
    module: {
      rules: [
        {
          test: /\.jsx?$/,
          exclude: /node_modules/,
          use: ["babel-loader"],
        },
        {
          test: /\.s?[ac]ss$/i,
          use: ["style-loader", "css-loader", "sass-loader"],
        },
      ],
    },
  };
};
