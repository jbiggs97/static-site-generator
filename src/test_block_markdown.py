import unittest

from block_markdown import (
    markdown_to_blocks,
    markdown_to_html    
)
import main

class TestTextNode(unittest.TestCase):

    def test_markdown_to_blocks(self):
        test_cases = [
            {
                'test': "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items",
                'expect': [
                        'This is **bolded** paragraph',
                        'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                        '* This is a list\n* with items'
                        ]

            },
            {
                'test': "\n\nThis is **bolded** paragraph\n\n\n   This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n\n",
                'expect': [
                        'This is **bolded** paragraph',
                        'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                        '* This is a list\n* with items'
                        ]

            }

        ]
        for case in test_cases:
            blocks = markdown_to_blocks(case['test'])
            for index, block in enumerate(blocks):
                self.assertEqual(block, case["expect"][index])


    def test_markdown_to_html(self):
        test_cases = [
            {
                'test': """# In arcus quae

## Flamina ira tecta Dictaeaque

Lorem [markdownum verba](http://est.org/), et solacia exstat nec furens. Voce
exasperat corpus, pro corpora enim quaecumque cum terra, pendet ense inque,;
urbes. Foret ense date ultricibus cultus protinus cadis spectat et herbae agitur
virago at alio, meruit. Achilles ventre mea mea; inquit pax anseribus caper.
Auro sonum: cum sol [Nam proles](http://www.fronti.io/inverbaque) lacerae
Pedasus in tamen At uti erat.

```digital_ieee += program_vdu_sequence(747324,
        registry.balancingData.host_system_ipv(languageIn,
        telnetTwitterPhp), formula_insertion_partition.numInternet(
        truncateListserv + 2, data_swappable));
if (memory(mbrFlatMirrored + 5)) {
    del.rwYahoo += searchForumSample(2, rjLog);
} else {
    double_usb(24863);
}
if (wanParityGoodput != unfriend_layout_utf) {
    infringement += hard(wired_down * restore_hoc, phreaking_parallel, 65);
}
var grayscaleCamelcaseSnow = beta(hertz_motion, ipModule + activeDvMetal(74,
        sla), botnet.disk_sidebar_irc(4));```

## Translata lacrimis hoc pietas sed quam nimiumque

Ut umero: inpulit meis glacies, in vicit cornua reverti, paulum iugulati merito
multa. Praeside bracchia vultu tamen, vota his mariti mihi curaque secum; auras
arma lora.""",
                'expect': """<h1>In arcus quae</h1>
<h2>Flamina ira tecta Dictaeaque</h2>
<p>Lorem <a href="http://est.org/">markdownum verba</a>, et solacia exstat nec furens. Voce
exasperat corpus, pro corpora enim quaecumque cum terra, pendet ense inque,;
urbes. Foret ense date ultricibus cultus protinus cadis spectat et herbae agitur
virago at alio, meruit. Achilles ventre mea mea; inquit pax anseribus caper.
Auro sonum: cum sol <a href="http://www.fronti.io/inverbaque">Nam proles</a> lacerae
Pedasus in tamen At uti erat.</p>
<pre><code>digital_ieee += program_vdu_sequence(747324,
        registry.balancingData.host_system_ipv(languageIn,
        telnetTwitterPhp), formula_insertion_partition.numInternet(
        truncateListserv + 2, data_swappable));
if (memory(mbrFlatMirrored + 5)) {
    del.rwYahoo += searchForumSample(2, rjLog);
} else {
    double_usb(24863);
}
if (wanParityGoodput != unfriend_layout_utf) {
    infringement += hard(wired_down * restore_hoc, phreaking_parallel, 65);
}
var grayscaleCamelcaseSnow = beta(hertz_motion, ipModule + activeDvMetal(74,
        sla), botnet.disk_sidebar_irc(4));</code></pre>
<h2>Translata lacrimis hoc pietas sed quam nimiumque</h2>
<p>Ut umero: inpulit meis glacies, in vicit cornua reverti, paulum iugulati merito
multa. Praeside bracchia vultu tamen, vota his mariti mihi curaque secum; auras
arma lora.</p>"""
            },
            {
                'test': """# This is my **Heading**

this is my paragraph

My unordered list below:

* List item 1
* List item 2
* *List* item 3""",
                'expect': """<h1>This is my <b>Heading</b></h1>
<p>this is my paragraph</p>
<p>My unordered list below:</p>
<ul><li>List item 1</li><li>List item 2</li><li><i>List</i> item 3</li></ul>"""
            }
        ]
        for case in test_cases:
            html_text = markdown_to_html(case['test'])
            self.assertEqual(html_text, case["expect"])


if __name__ == "__main__":
    unittest.main()