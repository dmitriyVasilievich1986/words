const path = require("path");

module.exports = (env, argv) => {
  return {
    entry: "./src/index.js",
    output: {
      filename: "main.js",
    },
    devtool: argv.mode === "development" ? "source-map" : "eval",
    resolve: {
      alias: {
        Reducers: path.resolve(__dirname, "src/reducers/"),
      },
    },
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
