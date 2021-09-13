import React, { Component } from "react";
import MenuItem from "@mui/material/MenuItem";

import CountryDetails from "./country_details.js";
import CountrySelect from "./country_select.js";

export default class CoronavirusData extends Component {
    constructor(props) {
        super(props);

        this.make_url = this.make_url.bind(this);
        this.make_request = this.make_request.bind(this);
        this.getCasesByCountry = this.getCasesByCountry.bind(this);
        this.handleValueChange = this.handleValueChange.bind(this);
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
            country: "India",
            cd: {},
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
        this.getCasesByCountry(this.state.country);
        this.getCountries();
    }

    getCountries() {
        var country_menu = [];
        const resPromise = this.stats.casesByCountry;
        resPromise.then((result) => {
            result.countries_stat.forEach((country_dets) => {
                country_menu.push(
                    <MenuItem
                        key={country_dets.country_name}
                        value={country_dets.country_name}
                    >
                        {country_dets.country_name}
                    </MenuItem>
                );
            });
            this.setState({ cm: country_menu });
        });
    }

    getCasesByCountry(country) {
        const resPromise = this.stats.casesByCountry;
        resPromise.then((result) => {
            let count_dets = result.countries_stat.find(dets => dets.country_name === country);
            this.setState({
                country: country,
                cd: count_dets,
            });
        });
    }

    handleValueChange(event) {
        this.getCasesByCountry(event.target.value);
    }

    render() {
        return (
            <div className="container">
                <CountrySelect
                    countries={this.state.cm}
                    value={this.state.country}
                    onValueChange={this.handleValueChange}
                />

                <CountryDetails
                    country={this.state.country}
                    details={this.state.cd}
                />
            </div>
        );
    }
}
