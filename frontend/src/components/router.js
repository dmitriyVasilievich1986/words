import CreateWordPage from "./pages/createWord/CreateWordPage";
import PhrasePage from "./pages/phrasePage/PhrasePage";
import React from "react";

import {
  createRoutesFromElements,
  createBrowserRouter,
  Route,
} from "react-router-dom";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route path="" element={<PhrasePage />} />
      <Route path="create" element={<CreateWordPage />} />
    </Route>
  )
);

export default router;
