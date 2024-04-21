import { useSearchParams } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

import CreateWord from "./CreateWord";
import UpdateWord from "./UpdateWord";
import WordsList from "./WordsList";

const cx = classnames.bind(style);

function CreateWordPage() {
  const [infinitives, setInfinitives] = React.useState([]);
  const [searchParams, setSearchParams] = useSearchParams();

  React.useEffect(() => {
    axios
      .get("/api/infinitive/")
      .then((response) => {
        setInfinitives(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className={cx("page")}>
      <div className={cx("side")}>
        <WordsList infinitives={infinitives} />
      </div>
      <div className={cx("center")}>
        {searchParams.get("infinitive") === null ? (
          <CreateWord setInfinitives={setInfinitives} />
        ) : (
          <UpdateWord
            pk={searchParams.get("infinitive")}
            setInfinitives={setInfinitives}
          />
        )}
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default CreateWordPage;
