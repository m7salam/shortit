module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "https://tier.app.s3.amazonaws.com"
      : "/",
  devServer: {
    proxy: {
      "^/api/": {
        target: "http://127.0.0.1:8000/",
        ws: false
      }
    }
  },
  // chainWebpack: config => {
  //   if (process.env.NODE_ENV === "production") {
  //     config.plugin("html").tap(args => {
  //       args[0].minify.removeAttributeQuotes = false;
  //       args[0].minify.removeComments = true;
  //       return args;
  //     });
  //   }
  // },
};
