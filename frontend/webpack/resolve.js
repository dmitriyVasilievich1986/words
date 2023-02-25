const path = require("path");

module.exports = {
  alias: {
    Constants: path.resolve(__dirname, "../src/constants.js"),
    Reducers: path.resolve(__dirname, "../src/reducers/"),
    Pages: path.resolve(__dirname, "../src/pages.js"),
  },
};
