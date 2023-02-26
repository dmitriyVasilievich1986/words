import CreateWordPage from "./components/pages/createWord/CreateWordPage";
import PhrasePage from "./components/pages/phrasePage/PhrasePage";

const PAGES = [
  {
    element: PhrasePage,
    hiden: false,
    name: "Home",
    path: "/",
  },
  {
    element: CreateWordPage,
    path: "/create",
    name: "Create",
    hiden: true,
  },
];

export default PAGES;
