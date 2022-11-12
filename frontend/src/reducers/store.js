import { configureStore } from "@reduxjs/toolkit";
import wordReducer from "./wordReducer";

export default configureStore({
  reducer: {
    words: wordReducer,
  },
});
