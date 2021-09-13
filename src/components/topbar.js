import React from "react";

import {AppBar} from "@mui/material";
import {Toolbar} from "@mui/material";
import {Typography} from "@mui/material";

function TopBar() {
    return (
        <AppBar position="static" color="inherit">
            <Toolbar>
                <Typography color="inherit" variant="h5">
                    Coronavirus Dashboard
                </Typography>
            </Toolbar>
        </AppBar>
    );
}

export default TopBar;
