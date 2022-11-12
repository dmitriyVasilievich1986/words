import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import store from "./reducers/store";
import App from "./components/App";
import "./styles/style.scss";
import React from "react";

const container = document.getElementById("app");
const root = createRoot(container);
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
