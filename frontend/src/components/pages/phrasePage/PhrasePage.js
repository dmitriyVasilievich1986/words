import { useSearchParams } from "react-router-dom";
import { Select } from "../mainComponents";
import classnames from "classnames/bind";
import PhraseForm from "./PhraseForm";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function PhrasePage() {
  const [searchParams, setSearchParams] = useSearchParams();

  const [rules, setRules] = React.useState([]);
  const [selectedRules, setSelectedRules] = React.useState(
    searchParams
      .get("rules")
      ?.split(",")
      ?.map((r) => Number(r)) || []
  );

  React.useEffect(() => {
    axios
      .get("api/rulesrandom/")
      .then((data) => {
        setRules(data.data);
      })
      .catch((e) => console.log(e));
  }, []);

  if (rules.length === 0) return <div>Loading...</div>;
  return (
    <div className={cx("page")}>
      <div className={cx("side", "left")}>
        <div>
          <Select
            multiple={true}
            value={selectedRules}
            options={rules.map((r) => ({ ...r, word: r.name }))}
            onChange={(items) => {
              setSearchParams(
                items.length > 0 ? { rules: items.join(",") } : {}
              );
              setSelectedRules(items);
            }}
          />
        </div>
      </div>
      <div className={cx("center")}>
        <PhraseForm selectedRules={selectedRules} rules={rules} />
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default PhrasePage;
