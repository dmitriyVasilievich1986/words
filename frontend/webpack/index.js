const path = require("path");

module.exports = (env, argv) => {
  return {
    devtool: argv.mode == "development" ? "source-map" : false,
    resolve: require("./resolve.js"),
    output: require("./output.js"),
    entry: require("./entry.js"),
    module: {
      ...require("./rules"),
    },
  };
};
