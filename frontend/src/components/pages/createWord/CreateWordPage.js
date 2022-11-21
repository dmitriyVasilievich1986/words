import CreateVerb from "./CreateVerb";
import CreateNoun from "./CreateNoun";
import CreateAdj from "./CreateAdj";
import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);
const pages = {
  createNoun: "создать существительное",
  createAdj: "создать прилагательное",
  createVerb: "создать глагол",
};

function CreateWordPage() {
  const [page, setPage] = React.useState(pages.createNoun);

  const pageName = () => {
    switch (page) {
      case pages.createNoun:
        return <CreateNoun />;
      case pages.createAdj:
        return <CreateAdj />;
      case pages.createVerb:
      default:
        return <CreateVerb />;
    }
  };

  return (
    <div className={cx("phrase-main")}>
      <div className={cx("phrase-side")}>
        <select
          className={cx("phrase-select")}
          value={page}
          onChange={(e) => setPage(e.target.value)}
        >
          {Object.values(pages).map((p) => (
            <option value={p} key={p}>
              {p}
            </option>
          ))}
        </select>
      </div>
      <div className={cx("phrase-center")}>
        <div className={cx("empty")} />
        {pageName()}
      </div>
      <div className={cx("phrase-side")} />
    </div>
  );
}

export default CreateWordPage;
