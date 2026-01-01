const express = require('express');
const router = express.Router();

// Message Page
router.get('/', (req, res) => res.render('messages'));

module.exports = router;
