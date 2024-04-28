import { useParams, useNavigate } from "react-router-dom";
import classnames from "classnames/bind";
import { Card } from "../../components";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function Verb(props) {
  const navigate = useNavigate();
  const params = useParams();

  const [personal_pronouns, setPersonal_pronouns] = React.useState([]);
  const [infinitive, setInfinitive] = React.useState(null);

  React.useEffect(() => {
    const url = params?.pk
      ? `/api/infinitive/${params.pk}/`
      : "/api/verb/empty/";
    Promise.all([axios.get(url), axios.get("/api/personal_pronoun/")])
      .then((response) => {
        const [infinitive, personal_pronouns] = response;
        setInfinitive({ ...infinitive.data });
        props.setTags(infinitive.data.tags.map((t) => t.tags));
        setPersonal_pronouns(personal_pronouns.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [params.pk]);

  const submitHandler = (e) => {
    e.preventDefault();
    const url = params?.pk
      ? `/api/infinitive/${params.pk}/`
      : "/api/infinitive/";
    const method = params?.pk ? "put" : "post";
    axios({
      method,
      url,
      data: { ...infinitive, tags: props.tags },
    })
      .then((response) => {
        setInfinitive({ ...response.data });
        props.setTags(infinitive.data.tags.map((t) => t.tags));
        navigate(`/create/verb/${response.data.id}`);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const updatePPVerb = ({ name, value }, ppId) => {
    setInfinitive((prev) => {
      const verb = prev.verb.map((v) =>
        v.personal_pronoun == ppId ? { ...v, [name]: value } : v
      );
      return { ...prev, verb };
    });
  };

  if (infinitive === null || personal_pronouns.length === 0) return null;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler}>
        <Card>
          <div className={cx("input-wrapper")}>
            <div className={cx("input-row")}>
              <label>Слово:</label>
              <input
                type="text"
                name="word"
                placeholder="Слово"
                value={infinitive.word}
                onChange={(e) =>
                  setInfinitive((prev) => ({ ...prev, word: e.target.value }))
                }
              />
            </div>
            <div className={cx("input-row")}>
              <label>Перевод:</label>
              <input
                type="text"
                name="translate"
                placeholder="Перевод"
                value={infinitive.translate}
                onChange={(e) =>
                  setInfinitive((prev) => ({
                    ...prev,
                    translate: e.target.value,
                  }))
                }
              />
            </div>
          </div>
        </Card>
        <Card>
          {personal_pronouns.map((personal_pronoun) => {
            const verb = infinitive.verb.find(
              (v) => v.personal_pronoun === personal_pronoun.id
            );
            return (
              <div
                key={personal_pronoun.id}
                className={cx("input-wrapper")}
                style={{ marginTop: "5px" }}
              >
                <div className={cx("input-row")}>
                  <label>{personal_pronoun.word}</label>
                  <input
                    type="text"
                    name="word"
                    placeholder="word"
                    value={verb.word}
                    onChange={(e) =>
                      updatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
                <div className={cx("input-row")}>
                  <label>{personal_pronoun.translate}</label>
                  <input
                    type="text"
                    name="translate"
                    placeholder="translate"
                    value={verb.translate}
                    onChange={(e) =>
                      updatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
              </div>
            );
          })}
        </Card>
        <div className={cx("send-button")}>
          <button>сохранить</button>
        </div>
      </form>
    </div>
  );
}

export default Verb;
