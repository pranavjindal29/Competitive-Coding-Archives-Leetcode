<h2><a href="https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring">Find the Occurrence of First Almost Equal Substring</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>You are given two strings <code>s</code> and <code>pattern</code>.</p>

<p>A string <code>x</code> is called <strong>almost equal</strong> to <code>y</code> if you can change <strong>at most</strong> one character in <code>x</code> to make it <em>identical</em> to <code>y</code>.</p>

<p>Return the <strong>smallest</strong> <em>starting index</em> of a <span data-keyword="substring-nonempty">substring</span> in <code>s</code> that is <strong>almost equal</strong> to <code>pattern</code>. If no such index exists, return <code>-1</code>.</p>
A <strong>substring</strong> is a contiguous <b>non-empty</b> sequence of characters within a string.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcdefg&quot;, pattern = &quot;bcdffg&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The substring <code>s[1..6] == &quot;bcdefg&quot;</code> can be converted to <code>&quot;bcdffg&quot;</code> by changing <code>s[4]</code> to <code>&quot;f&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ababbababa&quot;, pattern = &quot;bacaba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The substring <code>s[4..9] == &quot;bababa&quot;</code> can be converted to <code>&quot;bacaba&quot;</code> by changing <code>s[6]</code> to <code>&quot;c&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcd&quot;, pattern = &quot;dba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;dde&quot;, pattern = &quot;d&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt; s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>pattern</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem if <strong>at most</strong> <code>k</code> <strong>consecutive</strong> characters can be changed?