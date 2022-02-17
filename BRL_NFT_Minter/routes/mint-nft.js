const express = require('express');
const router = express.Router();
const minter = require('../scripts/mint-nft')
router.post('/', async (req,res) => {
    try {     
        const metaInfo = req.body;
        const link = metaInfo.file_link;
        const msg = await minter(link);
        res.send(200);
    } catch (err) {
        res.send(500).json({
            "Message":err
        });
    }
});

module.exports = router;