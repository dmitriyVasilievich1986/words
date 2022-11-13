const path = require("path");

module.exports = (dev) => {
  return {
    devtool: dev ? "source-map" : false,
    resolve: require("./resolve.js"),
    output: require("./output.js"),
    entry: require("./entry.js"),
    module: {
      ...require("./rules"),
    },
  };
};
