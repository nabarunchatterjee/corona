import React, { Component } from "react";

import {Box} from "@mui/material";
import {Card} from "@mui/material";
import {CardContent} from "@mui/material";
import {Divider} from "@mui/material";

import './country_details.css';

export default class CountryDetails extends Component {
    render() {
        const details = this.props.details;
        return (
            <Card className="card">
                <CardContent>
                    <h2 className="heading">{this.props.country}</h2>
                    <span className="subheader">
                        {this.props.country}
                    </span>
                </CardContent>
                <Divider light />
                <Box display={"flex"}>
                    <Box
                        className="box"
                        p={2}
                        flex={"auto"}
                    >
                        <p className="statlabel">Cases</p>
                        <p className="statvalue">{details.cases}</p>
                    </Box>
                    <Box
                        className="box"
                        p={2}
                        flex={"auto"}
                    >
                        <p className="statlabel">Deaths</p>
                        <p className="statvalue">{details.deaths}</p>
                    </Box>
                    <Box
                        className="box"
                        p={2}
                        flex={"auto"}
                    >
                        <p className="statlabel">Active</p>
                        <p className="statvalue">{details.active_cases}</p>
                    </Box>
                </Box>
                <Divider light />
                <Box display={"flex"}>
                    <Box
                        className="box"
                        p={2}
                        flex={"auto"}
                    >
                        <p className="statlabel">Tested</p>
                        <p className="statvalue">{details.total_tests}</p>
                    </Box>
                    <Box
                        className="box"
                        p={2}
                        flex={"auto"}
                    >
                        <p className="statlabel">Recovered</p>
                        <p className="statvalue">{details.total_recovered}</p>
                    </Box>
                </Box>
            </Card>
        );
    }
}
