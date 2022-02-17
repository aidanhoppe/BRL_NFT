const express = require('express');
const router = express.Router();

router.post('/', async (req,res) => {
    try {        
        res.json({
            "Test":"Testing complete"
        }).send(200);
    } catch (err) {
        res.send(500).json({
            "Message":err
        });
    }
});

module.exports = router;