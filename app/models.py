# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~

    Provides the SQLAlchemy models
"""
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from datetime import datetime as dt
from app import db


class Climate(db.Model):
    # auto keys
    id = db.Column(db.Integer, primary_key=True)
    utc_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow())
    utc_updated = db.Column(
        db.DateTime, nullable=False, default=dt.utcnow(), onupdate=dt.utcnow())

    # other keys
    rid = db.Column(db.String(128), unique=True)
    country = db.Column(db.String(64), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    annual = db.Column(db.Numeric)
    djf = db.Column(db.Numeric)
    mam = db.Column(db.Numeric)
    jja = db.Column(db.Numeric)
    son = db.Column(db.Numeric)
