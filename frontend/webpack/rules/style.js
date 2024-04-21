module.exports = {
  test: /\.s?[ac]ss$/i,
  use: [
    { loader: "style-loader" },
    {
      loader: "css-loader",
      options: {
        modules: {
          localIdentName: "[folder]__[local]",
        },
      },
    },
    { loader: "sass-loader" },
  ],
};
