import React from "react";
import {Select} from "@mui/material";
import {FormControl} from "@mui/material";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { useMinimalSelectStyles } from "@mui-treasury/styles/select/minimal";

const CountrySelect = (props) => {
    const minimalSelectClasses = useMinimalSelectStyles();

    const iconComponent = (props) => {
        return (
            <ExpandMoreIcon
                className={props.className + " " + minimalSelectClasses.icon}
            />
        );
    };

    // moves the menu below the select input
    const menuProps = {
        classes: {
            paper: minimalSelectClasses.paper,
            list: minimalSelectClasses.list,
        },
        anchorOrigin: {
            vertical: "bottom",
            horizontal: "right",
        },
        transformOrigin: {
            vertical: "top",
            horizontal: "right",
        },
    };

    return (
        <FormControl size="small">
            <Select
                classes={{ root: minimalSelectClasses.select }}
                MenuProps={menuProps}
                IconComponent={iconComponent}
                value={props.value}
                onChange={props.onValueChange}
            >
                {props.countries}
            </Select>
        </FormControl>
    );
};

export default CountrySelect;
