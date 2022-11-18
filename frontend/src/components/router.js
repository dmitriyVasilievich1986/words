import { createRoutesFromElements, createBrowserRouter, Route } from "react-router-dom";
import PhrasePage from "./pages/phrasePage/PhrasePage";
import React from "react";


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/">
            <Route path="" element={<PhrasePage />} />
        </Route>
    )
);

export default router