import CreateWordPage from "./components/pages/createWord/CreateWordPage";
import PhrasePage from "./components/pages/phrasePage/PhrasePage";
const PAGES = [
  {
    element: PhrasePage,
    name: "Home",
    path: "/",
  },
  {
    element: CreateWordPage,
    path: "/create",
    name: "Create",
  },
];

export default PAGES;
