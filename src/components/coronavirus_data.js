import React, { Component } from "react";

class CountryDetails extends Component {
    render() {
        return (
            <li key={this.props.country}>
                {this.props.country}: {this.props.cases}
            </li>
        );
    }
}

export default class CoronavirusData extends Component {
    constructor(props) {
        super(props);

        this.make_url = this.make_url.bind(this);
        this.make_request = this.make_request.bind(this);
        this.getCasesByCountry = this.getCasesByCountry.bind(this);
        this.urls = {
            casesByCountry: this.make_url("cases_by_country"),
            worldStats: this.make_url("worldstat"),
            casesByParticularCountry: this.make_url(
                "cases_by_particular_country"
            ),
            latestStatByCountry: this.make_url("latest_stat_by_country"),
        };

        this.stats = {
            casesByCountry: this.make_request(this.urls.casesByCountry),
        };

        this.state = {
            stats: {},
        };
    }

    make_url(stat) {
        const host = this.props.host;
        return `https://${host}/coronavirus/${stat}.php`;
    }

    make_request(url) {
        const resp = fetch(url, {
            method: "GET",
            headers: {
                "x-rapidapi-host": this.props.host,
                "x-rapidapi-key": this.props.api_key,
            },
        })
            .then((response) => response.json())
            .catch((err) => {
                console.error(err);
            });
        return resp;
    }

    componentDidMount() {
        this.getCasesByCountry();
    }

    getCasesByCountry() {
        const resPromise = this.stats.casesByCountry;
        resPromise.then((result) => {
            let count_dets = result.countries_stat.map((det, i) => {
                return (
                    <CountryDetails key={det.country_name}
                        country={det.country_name}
                        cases={det.cases}
                    />
                );
            });
            this.setState({ cd: count_dets });
        });
    }

    render() {
        return <ul>{this.state.cd}</ul>;
    }
}
