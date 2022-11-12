import { createSlice } from "@reduxjs/toolkit";

export const wordsSlice = createSlice({
  name: "words",
  initialState: {
    verbDeclension: [],
    verb: [],
    pron: [],
  },
  reducers: {
    setState: (state, action) => {
      return {
        ...state,
        ...action.payload,
      };
    },
  },
});

export const { setState } = wordsSlice.actions;

export default wordsSlice.reducer;
